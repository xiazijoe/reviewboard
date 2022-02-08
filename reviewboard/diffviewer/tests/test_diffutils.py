import kgb
from itertools import zip_longest
class BaseFileDiffAncestorTests(kgb.SpyAgency, TestCase):
        @self.spy_for(Repository.get_file, owner=Repository)
        def get_file(repo, path, revision, base_commit_id=None, context=None,
                     **kwargs):
                    pass
            raise FileNotFoundError(path=path,
                                    revision=revision,
                                    base_commit_id=base_commit_id,
                                    context=context)
                    op=kgb.SpyOpReturn(True))
    def test_with_file_lookup_context(self):
        """Testing get_original_file with FileLookupContext populated"""
        repository = self.create_repository()

        self.spy_on(repository.get_file,
                    op=kgb.SpyOpReturn(b'test'))

        diffset = self.create_diffset(
            repository=repository,
            base_commit_id='abc123',
            extra_data={
                'diffset_key': 'diffset_value',
            })
        diffcommit = self.create_diffcommit(
            repository=repository,
            diffset=diffset,
            extra_data={
                'diffcommit_key': 'diffcommit_value',
            })
        filediff = self.create_filediff(
            diffset,
            commit=diffcommit,
            extra_data={
                'filediff_key': 'filediff_value',
            })

        user = self.create_user()
        request = self.create_http_request(user=user)

        get_original_file(filediff=filediff,
                          request=request)

        self.assertSpyCallCount(repository.get_file, 1)

        context = repository.get_file.last_call.kwargs.get('context')
        self.assertIsNotNone(context)

        self.assertIs(context.request, request)
        self.assertIs(context.user, user)
        self.assertEqual(context.base_commit_id, 'abc123')
        self.assertEqual(context.diff_extra_data.get('diffset_key'),
                         'diffset_value')
        self.assertEqual(context.commit_extra_data.get('diffcommit_key'),
                         'diffcommit_value')
        self.assertEqual(context.file_extra_data.get('filediff_key'),
                         'filediff_value')

            self.assertIsInstance(line, str)