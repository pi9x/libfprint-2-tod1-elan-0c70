srpm:
	rpmbuild -bs --define "_sourcedir $(PWD)" --define "_srcrpmdir $(PWD)" libfprint-2-tod1-elan-0c70.spec
