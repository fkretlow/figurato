all: clean
	@python3 ./scripts/build.py

clean:
	@echo "removing previous versions"
	@rm -f ./redist/FiguratoB.otf ./redist/FiguratoT.otf
