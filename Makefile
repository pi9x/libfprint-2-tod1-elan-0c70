NAME := libfprint-2-tod1-elan-0c70

.PHONY: srpm
srpm:
	rpmbuild -bs \
		--define "_sourcedir $(CURDIR)" \
		--define "_srcrpmdir $(CURDIR)" \
		$(NAME).spec
