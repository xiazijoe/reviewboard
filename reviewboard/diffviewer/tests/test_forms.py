        self.repository.scmtool_id = 'mercurial'
        self.repository.save(update_fields=('tool', 'scmtool_id'))
        repository = self.create_repository(
            tool_name='Mercurial')
             b'@@ -1,1 +1,2 @@\n'
                                          request=None)
             b'@@ -1,1 +1,2 @@\n'
             b'@@ -1,2 +1,3 @@\n'
        self.assertEqual(filediff.source_revision,
                         revisions[1].decode('utf-8'))
            'new_unix_mode': '100644',
            'old_unix_mode': '100644',
                                          request=None)
        orig_use_abs_paths = scmtool.diffs_use_absolute_paths

        self.assertEqual(filediff.source_revision,
                         revisions[1].decode('utf-8'))
            'new_unix_mode': '100644',
            'old_unix_mode': '100644',
                                          request=None)
                'validation_info': validation_info.decode('utf-8'),
        expected_error = 'Expecting value: line 1 column 1 (char 0)'
            unicode:
        content = json.dumps(data).encode('utf-8')
        return base64.b64encode(content).decode('utf-8')