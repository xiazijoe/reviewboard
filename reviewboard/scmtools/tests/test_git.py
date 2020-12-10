from djblets.testing.decorators import add_fixtures
from reviewboard.scmtools.git import ShortSHA1Error, GitClient, GitTool
from reviewboard.testing.testcase import TestCase

        with open(filename, 'rb') as f:
        self.assertEqual(file.orig_filename, b'testing')
        self.assertEqual(file.modified_filename, b'testing')
        self.assertEqual(file.orig_file_details, b'e69de29')
        self.assertEqual(file.modified_file_details, b'bcae657')
                         b'diff --git a/testing b/testing')
        self.assertEqual(file.data.splitlines()[-1], b'+ADD')
        self.assertEqual(file.orig_filename, b'testing')
        self.assertEqual(file.modified_filename, b'testing')
        self.assertEqual(file.orig_file_details, b'e69de29')
        self.assertEqual(file.modified_file_details, b'bcae657')
                         b'diff --git a/testing b/testing')
        self.assertEqual(file.data.splitlines()[-1], b'+ADD')
        self.assertEqual(file.orig_filename, b'cfg/testcase.ini')
        self.assertEqual(file.modified_filename, b'cfg/testcase.ini')
        self.assertEqual(file.orig_file_details, b'cc18ec8')
        self.assertEqual(file.modified_file_details, b'5e70b73')
                         b'diff --git a/cfg/testcase.ini b/cfg/testcase.ini')
        self.assertEqual(file.data.splitlines()[-1], b'+db = pyunit')
        self.assertEqual(file.orig_filename, b'cfg/testcase.ini')
        self.assertEqual(file.modified_filename, b'cfg/testcase.ini')
        self.assertEqual(file.orig_file_details, b'cc18ec8')
        self.assertEqual(file.modified_file_details, b'5e70b73')
                         b'diff --git a/cfg/testcase.ini b/cfg/testcase.ini')
        self.assertEqual(file.data.splitlines()[-1], b'+db = pyunit')
        self.assertEqual(file.orig_filename,
                         'cfg/téstcase.ini'.encode('utf-8'))
        self.assertEqual(file.modified_filename,
                         'cfg/téstcase.ini'.encode('utf-8'))
        self.assertEqual(file.orig_file_details, b'cc18ec8')
        self.assertEqual(file.modified_file_details, b'5e70b73')
        self.assertEqual(file.data.splitlines()[-1],
                         '+db = pyunít'.encode('utf-8'))
        self.assertEqual(files[0].orig_filename, b'README')
        self.assertEqual(files[0].modified_filename, b'README')
        self.assertEqual(files[0].orig_file_details,
                         b'712544e4343bf04967eb5ea80257f6c64d6f42c7')
        self.assertEqual(files[0].modified_file_details,
                         b'f88b7f15c03d141d0bb38c8e49bb6c411ebfe1f1')
        self.assertEqual(file.orig_filename, b'IAMNEW')
        self.assertEqual(file.modified_filename, b'IAMNEW')
        self.assertEqual(file.orig_file_details, PRE_CREATION)
        self.assertEqual(file.modified_file_details, b'e69de29')
                         b'diff --git a/IAMNEW b/IAMNEW')
        self.assertEqual(file.data.splitlines()[-1], b'+Hello')
        self.assertEqual(file.orig_filename, b'newfile')
        self.assertEqual(file.modified_filename, b'newfile')
        self.assertEqual(file.orig_file_details, PRE_CREATION)
        self.assertEqual(file.modified_file_details, b'e69de29')
        self.assertEqual(lines[0], b'diff --git a/newfile b/newfile')
        self.assertEqual(files[0].orig_filename, b'newfile')
        self.assertEqual(files[0].modified_filename, b'newfile')
        self.assertEqual(files[0].orig_file_details, PRE_CREATION)
        self.assertEqual(files[0].modified_file_details, b'e69de29')
        self.assertEqual(lines[0], b'diff --git a/newfile b/newfile')
        self.assertEqual(files[1].orig_filename, b'cfg/testcase.ini')
        self.assertEqual(files[1].modified_filename, b'cfg/testcase.ini')
        self.assertEqual(files[1].orig_file_details, b'cc18ec8')
        self.assertEqual(files[1].modified_file_details, b'5e70b73')
                         b'diff --git a/cfg/testcase.ini b/cfg/testcase.ini')
        self.assertEqual(lines[-1], b'+db = pyunit')
        self.assertEqual(file.orig_filename, b'OLDFILE')
        self.assertEqual(file.modified_filename, b'OLDFILE')
        self.assertEqual(file.orig_file_details, b'8ebcb01')
        self.assertEqual(file.modified_file_details, b'0000000')
                         b'diff --git a/OLDFILE b/OLDFILE')
        self.assertEqual(file.data.splitlines()[-1], b'-Goodbye')
        self.assertEqual(files[0].orig_filename, b'empty')
        self.assertEqual(files[0].modified_filename, b'empty')
        self.assertEqual(files[0].orig_file_details,
                         b'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
        self.assertEqual(files[0].modified_file_details,
                         b'0000000000000000000000000000000000000000')
                         b'diff --git a/empty b/empty')
        self.assertEqual(files[0].orig_filename, b'empty')
        self.assertEqual(files[0].modified_filename, b'empty')
        self.assertEqual(files[0].orig_file_details,
                         b'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
        self.assertEqual(files[0].modified_file_details,
                         b'0000000000000000000000000000000000000000')
                         b'diff --git a/empty b/empty')
        self.assertEqual(files[1].orig_filename, b'foo/bar')
        self.assertEqual(files[1].modified_filename, b'foo/bar')
        self.assertEqual(files[1].orig_file_details,
                         b'484ba93ef5b0aed5b72af8f4e9dc4cfd10ef1a81')
        self.assertEqual(files[1].modified_file_details,
                         b'0ae4095ddfe7387d405bd53bd59bbb5d861114c5')
        self.assertEqual(lines[0], b'diff --git a/foo/bar b/foo/bar')
        self.assertEqual(lines[5], b'+Hello!')
        self.assertEqual(file.orig_filename, b'pysvn-1.5.1.tar.gz')
        self.assertEqual(file.modified_filename, b'pysvn-1.5.1.tar.gz')
        self.assertEqual(file.orig_file_details, PRE_CREATION)
        self.assertEqual(file.modified_file_details, b'86b520c')
            lines[0],
            b'diff --git a/pysvn-1.5.1.tar.gz b/pysvn-1.5.1.tar.gz')
            lines[3],
            b'Binary files /dev/null and b/pysvn-1.5.1.tar.gz differ')
    def test_git_new_single_binary_diff(self):
        """Testing parsing Git diff with base64 binary and a new file"""
        diff = self._read_fixture('git_new_single_binary.diff')

        files = self.tool.get_parser(diff).parse()
        self.assertEqual(len(files), 2)

        self.assertEqual(files[0].orig_filename, b'Checked.svg')
        self.assertEqual(files[0].modified_filename, b'Checked.svg')
        self.assertFalse(files[0].binary)
        self.assertFalse(files[0].deleted)
        self.assertFalse(files[0].is_symlink)
        self.assertEqual(files[0].insert_count, 9)
        self.assertEqual(files[0].delete_count, 0)
        self.assertEqual(len(files[0].data), 969)
        split = files[0].data.splitlines()
        self.assertEqual(split[0], b'diff --git a/Checked.svg b/Checked.svg')
        self.assertEqual(split[-1], b'+</svg>')

        self.assertEqual(files[1].orig_filename, b'dialog.jpg')
        self.assertEqual(files[1].modified_filename, b'dialog.jpg')
        self.assertEqual(files[1].orig_file_details,
                         b'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
        self.assertEqual(files[1].modified_file_details,
                         b'5503573346e25878d57775ed7caf88f2eb7a7d98')
        self.assertTrue(files[1].binary)
        self.assertFalse(files[1].deleted)
        self.assertFalse(files[1].is_symlink)
        self.assertEqual(files[1].insert_count, 0)
        self.assertEqual(files[1].delete_count, 0)
        self.assertEqual(len(files[1].data), 42513)
        split = files[1].data.splitlines()
        self.assertEqual(split[0], b'diff --git a/dialog.jpg b/dialog.jpg')
        self.assertEqual(split[3], b'GIT binary patch')
        self.assertEqual(split[4], b'literal 34445')
        self.assertEqual(split[-2], (b'q75*tM8SetfV1Lcj#Q^wI3)5>pmuS8'
                                     b'x#<EIC&-<U<r2qLm&;Nht|C_x4'))

    def test_git_new_binaries_diff(self):
        """Testing parsing Git diff with base64 binaries and new files"""
        diff = self._read_fixture('git_new_binaries.diff')

        files = self.tool.get_parser(diff).parse()
        self.assertEqual(len(files), 3)

        self.assertEqual(files[0].orig_filename, b'other.png')
        self.assertEqual(files[0].modified_filename, b'other.png')
        self.assertEqual(files[0].orig_file_details,
                         b'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
        self.assertEqual(files[0].modified_file_details,
                         b'fddeadc701ac6dd751b8fc70fe128bd29e54b9b0')
        self.assertTrue(files[0].binary)
        self.assertFalse(files[0].deleted)
        self.assertFalse(files[0].is_symlink)
        self.assertEqual(files[0].insert_count, 0)
        self.assertEqual(files[0].delete_count, 0)
        self.assertEqual(len(files[0].data), 2007)
        split = files[0].data.splitlines()
        self.assertEqual(split[0], b'diff --git a/other.png b/other.png')
        self.assertEqual(split[3], b'GIT binary patch')
        self.assertEqual(split[4], b'literal 1459')
        self.assertEqual(split[-2], b'PuWv&b7#dLSFWLP!d=7XA')

        self.assertEqual(files[1].orig_filename, b'initial.png')
        self.assertEqual(files[1].modified_filename, b'initial.png')
        self.assertEqual(files[1].orig_file_details,
                         b'fddeadc701ac6dd751b8fc70fe128bd29e54b9b0')
        self.assertEqual(files[1].modified_file_details,
                         b'532716ada15dc62ddf8c59618b926f34d4727d77')
        self.assertTrue(files[1].binary)
        self.assertFalse(files[1].deleted)
        self.assertFalse(files[1].is_symlink)
        self.assertEqual(files[1].insert_count, 0)
        self.assertEqual(files[1].delete_count, 0)
        self.assertEqual(len(files[1].data), 10065)
        split = files[1].data.splitlines()
        self.assertEqual(split[0], b'diff --git a/initial.png b/initial.png')
        self.assertEqual(split[2], b'GIT binary patch')
        self.assertEqual(split[3], b'literal 7723')
        self.assertEqual(split[-2], (b'qU@utQTCoRZj8p;!(2CJ;Kce7Up0C'
                                     b'cmx5xf(jw;BgNY_Z3hW;Oyu4s(_'))

        self.assertEqual(files[2].orig_filename, b'xtxt.txt')
        self.assertEqual(files[2].modified_filename, b'xtxt.txt')
        self.assertFalse(files[2].binary)
        self.assertFalse(files[2].deleted)
        self.assertFalse(files[2].is_symlink)
        self.assertEqual(files[2].insert_count, 1)
        self.assertEqual(files[2].delete_count, 0)
        self.assertEqual(len(files[2].data), 107)
        split = files[2].data.splitlines()
        self.assertEqual(split[0], b'diff --git a/xtxt.txt b/xtxt.txt')
        self.assertEqual(split[-2], b'+Hello')

        self.assertEqual(files[0].orig_filename, b'cfg/testcase.ini')
        self.assertEqual(files[0].modified_filename, b'cfg/testcase.ini')
        self.assertEqual(files[0].orig_file_details, b'5e35098')
        self.assertEqual(files[0].modified_file_details, b'e254ef4')
                         b'diff --git a/cfg/testcase.ini b/cfg/testcase.ini')
                         b'         if isinstance(value, basestring):')
        self.assertEqual(files[1].orig_filename, b'tests/models.py')
        self.assertEqual(files[1].modified_filename, b'tests/models.py')
        self.assertEqual(files[1].orig_file_details, PRE_CREATION)
        self.assertEqual(files[1].modified_file_details, b'e69de29')
                         b'diff --git a/tests/models.py b/tests/models.py')
        self.assertEqual(files[2].orig_filename, b'tests/tests.py')
        self.assertEqual(files[2].modified_filename, b'tests/tests.py')
        self.assertEqual(files[2].orig_file_details, PRE_CREATION)
        self.assertEqual(files[2].modified_file_details, b'e279a06')
                         b'diff --git a/tests/tests.py b/tests/tests.py')
                         b'+This is some new content')
        self.assertEqual(files[3].orig_filename, b'pysvn-1.5.1.tar.gz')
        self.assertEqual(files[3].modified_filename, b'pysvn-1.5.1.tar.gz')
        self.assertEqual(files[3].orig_file_details, PRE_CREATION)
        self.assertEqual(files[3].modified_file_details, b'86b520c')
            lines[0], b'diff --git a/pysvn-1.5.1.tar.gz b/pysvn-1.5.1.tar.gz')
                         b'Binary files /dev/null and b/pysvn-1.5.1.tar.gz '
                         b'differ')
        self.assertEqual(files[4].orig_filename, b'readme')
        self.assertEqual(files[4].modified_filename, b'readme')
        self.assertEqual(files[4].orig_file_details, b'5e35098')
        self.assertEqual(files[4].modified_file_details, b'e254ef4')
        self.assertEqual(lines[0], b'diff --git a/readme b/readme')
        self.assertEqual(lines[6], b'+Hello there')
        self.assertEqual(files[5].orig_filename, b'OLDFILE')
        self.assertEqual(files[5].modified_filename, b'OLDFILE')
        self.assertEqual(files[5].orig_file_details, b'8ebcb01')
        self.assertEqual(files[5].modified_file_details, b'0000000')
        self.assertEqual(lines[0], b'diff --git a/OLDFILE b/OLDFILE')
        self.assertEqual(lines[6], b'-Goodbye')
        self.assertEqual(files[6].orig_filename, b'readme2')
        self.assertEqual(files[6].modified_filename, b'readme2')
        self.assertEqual(files[6].orig_file_details, b'5e43098')
        self.assertEqual(files[6].modified_file_details, b'e248ef4')
        self.assertEqual(lines[0], b'diff --git a/readme2 b/readme2')
        self.assertEqual(lines[6], b'+Hello there')
        self.assertEqual(files[0].orig_filename, b'foo/bar')
        self.assertEqual(files[0].modified_filename, b'foo/bar2')
        self.assertEqual(files[0].orig_file_details,
                         b'612544e4343bf04967eb5ea80257f6c64d6f42c7')
        self.assertEqual(files[0].modified_file_details,
                         b'e88b7f15c03d141d0bb38c8e49bb6c411ebfe1f1')
        self.assertEqual(files[0].orig_filename, b'foo.bin')
        self.assertEqual(files[0].modified_filename, b'foo.bin')
        self.assertEqual(files[1].orig_filename, b'bar.bin')
        self.assertEqual(files[1].modified_filename, b'bar.bin')
        self.assertEqual(files[0].orig_filename, b'foo/bar')
        self.assertEqual(files[0].modified_filename, b'foo/bar2')
        self.assertEqual(files[0].orig_file_details,
                         b'612544e4343bf04967eb5ea80257f6c64d6f42c7')
        self.assertEqual(files[0].modified_file_details,
                         b'e88b7f15c03d141d0bb38c8e49bb6c411ebfe1f1')
        self.assertEqual(files[1].orig_filename, b'README')
        self.assertEqual(files[1].modified_filename, b'README')
        self.assertEqual(files[1].orig_file_details,
                         b'712544e4343bf04967eb5ea80257f6c64d6f42c7')
        self.assertEqual(files[1].modified_file_details,
                         b'f88b7f15c03d141d0bb38c8e49bb6c411ebfe1f1')
            self.tool.parse_diff_revision(filename=b'doc/readme',
                                          revision=b'bf544ea'),
            (b'doc/readme', b'bf544ea'))
            self.tool.parse_diff_revision(filename=b'/dev/null',
                                          revision=b'bf544ea'),
            (b'/dev/null', PRE_CREATION))
            self.tool.parse_diff_revision(filename=b'/dev/null',
                                          revision=b'0000000'),
            (b'/dev/null', PRE_CREATION))
        self.assertEqual(f.orig_filename, b'foo/bar')
        self.assertEqual(f.modified_filename, b'foo/bar2')
        self.assertEqual(f.orig_file_details, b'')
        self.assertEqual(f.modified_file_details, b'')
        self.assertEqual(f.orig_filename, b'foo/bar')
        self.assertEqual(f.modified_filename, b'foo/bar3')
        self.assertEqual(f.orig_file_details,
                         b'612544e4343bf04967eb5ea80257f6c64d6f42c7')
        self.assertEqual(f.modified_file_details,
                         b'e88b7f15c03d141d0bb38c8e49bb6c411ebfe1f1')
        self.assertEqual(f.orig_filename, b'foo/bar')
        self.assertEqual(f.modified_filename, b'foo/bar2')
        self.assertEqual(f.orig_file_details,
                         b'612544e4343bf04967eb5ea80257f6c64d6f42c7')
        self.assertEqual(f.modified_file_details,
                         b'e88b7f15c03d141d0bb38c8e49bb6c411ebfe1f1')
        self.assertEqual(f.orig_filename, b'foo')
        self.assertEqual(f.modified_filename, b'foo')
        self.assertEqual(f.orig_filename, b'foo')
        self.assertEqual(f.modified_filename, b'foo')
        self.assertEqual(f.orig_filename, b'foo bar1')
        self.assertEqual(f.modified_filename, b'foo bar1')
        self.assertEqual(f.orig_filename, b'foo bar1')
        self.assertEqual(f.modified_filename, b'foo bar1')
        self.assertEqual(f.orig_filename, b'foo bar1')
        self.assertEqual(f.modified_filename, b'foo bar2')
        self.assertEqual(f.orig_filename, b'foo bar1')
        self.assertEqual(f.modified_filename, b'foo')
        self.assertEqual(f.orig_filename, b'foo')
        self.assertEqual(f.modified_filename, b'foo bar1')
        self.assertEqual(f.orig_file_details, PRE_CREATION)
        self.assertEqual(f.modified_filename, b'link')
        self.assertEqual(f.modified_filename, b'link')
        self.assertEqual(f.orig_filename, b'link')
        self.assertEqual(f.orig_filename, b'link')
        tool = self.tool

        self.assertTrue(tool.file_exists('readme', 'e965047'))
        self.assertTrue(tool.file_exists('readme', 'd6613f5'))
        self.assertFalse(tool.file_exists('readme', PRE_CREATION))
        self.assertFalse(tool.file_exists('readme', 'fffffff'))
        self.assertFalse(tool.file_exists('readme2', 'fffffff'))
        # These sha's are valid, but commit and tree objects, not blobs.
        self.assertFalse(tool.file_exists('readme', 'a62df6c'))
        self.assertFalse(tool.file_exists('readme2', 'ccffbb4'))
        tool = self.tool

        content = tool.get_file('readme', PRE_CREATION)
        self.assertIsInstance(content, bytes)
        self.assertEqual(content, b'')

        content = tool.get_file('readme', 'e965047')
        self.assertIsInstance(content, bytes)
        self.assertEqual(content, b'Hello\n')

        content = tool.get_file('readme', 'd6613f5')
        self.assertIsInstance(content, bytes)
        self.assertEqual(content, b'Hello there\n')
        content = tool.get_file('readme')
        self.assertIsInstance(content, bytes)
        self.assertEqual(content, b'Hello there\n')
        with self.assertRaises(SCMError):
            tool.get_file('')
        with self.assertRaises(FileNotFoundError):
            tool.get_file('', '0000000')

        with self.assertRaises(FileNotFoundError):
            tool.get_file('hello', '0000000')

        with self.assertRaises(FileNotFoundError):
            tool.get_file('readme', '0000000')
        with self.assertRaises(ShortSHA1Error):
            self.remote_tool.parse_diff_revision(filename=b'README',
                                                 revision=b'd7e96b3')
        with self.assertRaises(ShortSHA1Error):
            self.remote_tool.get_file('README', 'd7e96b3')


class GitAuthFormTests(TestCase):
    """Unit tests for GitTool's authentication form."""

    def test_fields(self):
        """Testing GitTool authentication form fields"""
        form = GitTool.create_auth_form()

        self.assertEqual(list(form.fields), ['username', 'password'])
        self.assertEqual(form['username'].help_text, '')
        self.assertEqual(form['username'].label, 'Username')
        self.assertEqual(form['password'].help_text, '')
        self.assertEqual(form['password'].label, 'Password')

    @add_fixtures(['test_scmtools'])
    def test_load(self):
        """Tetting GitTool authentication form load"""
        repository = self.create_repository(
            tool_name='Git',
            username='test-user',
            password='test-pass')

        form = GitTool.create_auth_form(repository=repository)
        form.load()

        self.assertEqual(form['username'].value(), 'test-user')
        self.assertEqual(form['password'].value(), 'test-pass')

    @add_fixtures(['test_scmtools'])
    def test_save(self):
        """Tetting GitTool authentication form save"""
        repository = self.create_repository(tool_name='Git')

        form = GitTool.create_auth_form(
            repository=repository,
            data={
                'username': 'test-user',
                'password': 'test-pass',
            })
        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(repository.username, 'test-user')
        self.assertEqual(repository.password, 'test-pass')


class GitRepositoryFormTests(TestCase):
    """Unit tests for GitTool's repository form."""

    def test_fields(self):
        """Testing GitTool repository form fields"""
        form = GitTool.create_repository_form()

        self.assertEqual(list(form.fields),
                         ['path', 'mirror_path', 'raw_file_url'])
        self.assertEqual(form['path'].help_text,
                         'For local Git repositories, this should be the path '
                         'to a .git directory that Review Board can read '
                         'from. For remote Git repositories, it should be '
                         'the clone URL.')
        self.assertEqual(form['path'].label, 'Path')
        self.assertEqual(form['mirror_path'].help_text, '')
        self.assertEqual(form['mirror_path'].label, 'Mirror Path')
        self.assertEqual(form['raw_file_url'].label, 'Raw File URL Mask')
        self.assertEqual(form['raw_file_url'].help_text,
                         "A URL mask used to check out a particular revision "
                         "of a file using HTTP. This is needed for "
                         "repository types that can't access remote files "
                         "natively. Use <tt>&lt;revision&gt;</tt> and "
                         "<tt>&lt;filename&gt;</tt> in the URL in place of "
                         "the revision and filename parts of the path.")

    @add_fixtures(['test_scmtools'])
    def test_load(self):
        """Tetting GitTool repository form load"""
        repository = self.create_repository(
            tool_name='Git',
            path='https://github.com/reviewboard/reviewboard',
            mirror_path='git@github.com:reviewboard/reviewboard.git',
            raw_file_url='http://git.example.com/raw/<revision>')

        form = GitTool.create_repository_form(repository=repository)
        form.load()

        self.assertEqual(form['path'].value(),
                         'https://github.com/reviewboard/reviewboard')
        self.assertEqual(form['mirror_path'].value(),
                         'git@github.com:reviewboard/reviewboard.git')
        self.assertEqual(form['raw_file_url'].value(),
                         'http://git.example.com/raw/<revision>')

    @add_fixtures(['test_scmtools'])
    def test_save(self):
        """Tetting GitTool repository form save"""
        repository = self.create_repository(tool_name='Git')

        form = GitTool.create_repository_form(
            repository=repository,
            data={
                'path': 'https://github.com/reviewboard/reviewboard',
                'mirror_path': 'git@github.com:reviewboard/reviewboard.git',
                'raw_file_url': 'http://git.example.com/raw/<revision>',
            })
        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(repository.path,
                         'https://github.com/reviewboard/reviewboard')
        self.assertEqual(repository.mirror_path,
                         'git@github.com:reviewboard/reviewboard.git')
        self.assertEqual(repository.raw_file_url,
                         'http://git.example.com/raw/<revision>')