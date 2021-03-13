# -*- coding:utf-8 -*-

def test_tmpdir(tmpdir):
    print(tmpdir)
    a_file = tmpdir.join('something.txt')

    a_sub_dir = tmpdir.mkdir('anything')

    anthor_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents ........')

    assert a_file.read() == 'contents ........'

