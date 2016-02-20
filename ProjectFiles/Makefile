DIRS = Source
#When libs are needed, uncomment libs
#LIBS = 
OUTPUTNAME = OpenIntelLinux

CPPCOMPILE = $(foreach dir, $(DIRS), $(wildcard $(dir)/*.cpp))

#when libs are needed, use commented line instead
all: $(CPPCOMPILE)
	#g++ $(CPPCOMPILE) -w $(LIBS) -o Executables/$(OUTPUTNAME)
	g++ $(CPPCOMPILE) -o Executables/$(OUTPUTNAME)
