from unittest.mock import patch, Mock

from drucker_dashboard.protobuf import drucker_pb2
from .base import BaseTestCase, create_app_obj, create_user_obj, create_application_user_role_obj, db, Application, ApplicationUserRole
from drucker_dashboard.server import create_app
from drucker_dashboard.models import Role


class ApiAccessControlTest(BaseTestCase):
    def create_app(self):
        return create_app("test/test-auth-settings.yml")

    @patch('drucker_dashboard.auth.authenticator.EmptyAuthenticator.auth_user')
    def _get_token(self, mock):
        mock.return_value = {'uid': 'test', 'name': 'TEST USER'}
        response = self.client.post('/api/login', content_type='application/json', data='{}')
        self.assertEqual(200, response.status_code)
        return response.json['jwt']

    def test_authentication_failure(self):
        response = self.client.get('/api/applications/')
        self.assertEqual(401, response.status_code)

    def test_authentication_success(self):
        token = self._get_token()
        response = self.client.get('/api/applications/', headers={'Authorization': 'Bearer {}'.format(token)})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json))

    @patch('drucker_dashboard.drucker_dashboard_client.drucker_pb2_grpc.DruckerDashboardStub')
    def test_create_appliction(self, mock):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}

        mock_stub_obj = Mock()
        mock_stub_obj.ServiceInfo.return_value = drucker_pb2.ServiceInfoResponse()
        mock.return_value = mock_stub_obj

        data = {'host': 'localhost:5000'}
        response = self.client.post('/api/applications/', headers=headers, data=data)
        self.assertEqual(200, response.status_code)

    @patch('drucker_dashboard.drucker_dashboard_client.drucker_pb2_grpc.DruckerDashboardStub')
    def test_create_appliction_already_exist(self, mock):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}

        aobj = create_app_obj(kubernetes_id=None, save=True)
        uobj = create_user_obj(auth_id='test', user_name='TEST USER')
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, role=Role.owner)
        self.assertIsNotNone(robj)

        # return same application_name
        mock_stub_obj = Mock()
        mock_stub_obj.ServiceInfo.return_value = drucker_pb2.ServiceInfoResponse(
            application_name=aobj.application_name,
            service_name='new-service-name')
        mock.return_value = mock_stub_obj

        data = {'host': 'localhost:5000'}
        response = self.client.post('/api/applications/', headers=headers, data=data)
        self.assertEqual(200, response.status_code)

    def test_get_applications_list(self):
        token = self._get_token()
        aobj = create_app_obj(kubernetes_id=2, save=True)

        response = self.client.get('/api/applications/', headers={'Authorization': 'Bearer {}'.format(token)})
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.json))

        # other user become the owner of `aobj` and test user cannot access
        uobj = create_user_obj(auth_id='test2', user_name='TEST USER 2', save=True)
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, role=Role.owner)
        self.assertIsNotNone(robj)

        response = self.client.get('/api/applications/', headers={'Authorization': 'Bearer {}'.format(token)})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json))

    def test_edit_application_by_viewer(self):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}
        data = {'description': 'description'}
        aobj = create_app_obj()
        uobj = create_user_obj(auth_id='test', user_name='TEST USER')
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, role=Role.viewer)
        self.assertIsNotNone(robj)

        response = self.client.patch('/api/applications/{}'.format(aobj.application_id), headers=headers, data=data)
        self.assertEqual(401, response.status_code)

    def test_edit_application_by_editor(self):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}
        data = {'description': 'description'}
        aobj = create_app_obj()
        uobj = create_user_obj(auth_id='test', user_name='TEST USER')
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, role=Role.editor)
        self.assertIsNotNone(robj)

        response = self.client.patch('/api/applications/{}'.format(aobj.application_id), headers=headers, data=data)
        self.assertEqual(200, response.status_code)

    def test_edit_application_by_owner(self):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}
        data = {'description': 'description'}
        aobj = create_app_obj()
        uobj = create_user_obj(auth_id='test', user_name='TEST USER')
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, role=Role.owner)
        self.assertIsNotNone(robj)

        response = self.client.patch('/api/applications/{}'.format(aobj.application_id), headers=headers, data=data)
        self.assertEqual(200, response.status_code)

    def test_delete_application(self):
        aobj = create_app_obj()
        uobj = create_user_obj(auth_id='test', user_name='TEST USER', save=True)
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, role=Role.owner)
        self.assertIsNotNone(robj)

        db.session.delete(aobj)
        db.session.flush()
        num = db.session.query(ApplicationUserRole).filter(ApplicationUserRole.application_id == aobj.application_id).count()
        self.assertEqual(0, num)

    def test_get_users(self):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}
        aobj = create_app_obj()
        uobj = create_user_obj(auth_id='test', user_name='TEST USER')
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id)
        self.assertIsNotNone(robj)

        # viewer
        robj.role = Role.viewer
        response = self.client.get('/api/applications/{}/acl'.format(aobj.application_id), headers=headers)
        self.assertEqual(401, response.status_code)

        # editor
        robj.role = Role.editor
        response = self.client.get('/api/applications/{}/acl'.format(aobj.application_id), headers=headers)
        self.assertEqual(401, response.status_code)

        # owner
        robj.role = Role.owner
        response = self.client.get('/api/applications/{}/acl'.format(aobj.application_id), headers=headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json))

    def test_add_user_success(self):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}
        aobj = create_app_obj()
        uobj = create_user_obj(auth_id='otheruser', user_name='OTHER USER', save=True)

        data = {'uid': uobj.auth_id, 'role': Role.viewer.name}
        response = self.client.post('/api/applications/{}/acl'.format(aobj.application_id), headers=headers, data=data)
        self.assertEqual(200, response.status_code)

    def test_add_user_with_invalid_role(self):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}
        aobj = create_app_obj()
        uobj = create_user_obj(auth_id='otheruser', user_name='OTHER USER', save=True)

        # invalid role
        data = {'uid': uobj.auth_id, 'role': 'cracker'}
        response = self.client.post('/api/applications/{}/acl'.format(aobj.application_id), headers=headers, data=data)
        self.assertEqual(400, response.status_code)

    def test_add_user_already_exist(self):
        token = self._get_token()
        headers = {'Authorization': 'Bearer {}'.format(token)}
        aobj = create_app_obj()

        uobj = create_user_obj(auth_id='test', user_name='TEST USER')
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, role=Role.owner, save=True)
        self.assertIsNotNone(robj)
        uobj = create_user_obj(auth_id='otheruser', user_name='OTHER USER', save=True)
        robj = create_application_user_role_obj(application_id=aobj.application_id, user_id=uobj.user_id, save=True)
        self.assertIsNotNone(robj)

        data = {'uid': uobj.auth_id, 'role': Role.viewer.name}
        response = self.client.post('/api/applications/{}/acl'.format(aobj.application_id), headers=headers, data=data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('Already exist.', response.json['message'])
