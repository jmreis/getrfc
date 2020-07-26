PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin
MANDIR ?= $(PREFIX)/share/man/man1
DOCDIR ?= $(PREFIX)/share/doc/getrfc

.PHONY: all install uninstall

all:

install:
	install -m755 -d $(DESTDIR)$(BINDIR)
	install -m755 -d $(DESTDIR)$(MANDIR)
	install -m755 -d $(DESTDIR)$(DOCDIR)
	gzip -c getrfc.1 > getrfc.1.gz
	install -m755 getrfc $(DESTDIR)$(BINDIR)
	install -m644 getrfc.1.gz $(DESTDIR)$(MANDIR)
	install -m644 README.md $(DESTDIR)$(DOCDIR)
	rm -f getrfc.1.gz

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/getrfc
	rm -f $(DESTDIR)$(MANDIR)/getrfc.1.gz
	rm -rf $(DESTDIR)$(DOCDIR)

test:
	./getrfc --help
