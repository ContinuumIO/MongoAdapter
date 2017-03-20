CC = gcc
CFLAGS = -g -Werror -Wall -Wdeclaration-after-statement
TEXT_INCLUDE_DIRS = -I ../textadapter -I ../lib
TEXT_LIBS = -lz -lpcre
MONGO_INCLUDE_DIRS = -I ../mongoadapter -I ../lib
MONGO_LIBS = -lmongoc
MONGO_OBJS = test_mongo_adapter.o mongo_adapter.o converter_functions.o field_info.o

test_mongo_adapter: $(MONGO_OBJS)
	$(CC) $(CFLAGS) $(MONGO_OBJS) -o test_mongo_adapter $(MONGO_LIBS)

test_mongo_adapter.o: test_mongo_adapter.c
	$(CC) $(CFLAGS) -c test_mongo_adapter.c $(MONGO_INCLUDE_DIRS)

mongo_adapter.o: ../mongoadapter/mongo_adapter.c
	$(CC) $(CFLAGS) -c ../mongoadapter/mongo_adapter.c $(MONGO_INCLUDE_DIRS)

converter_functions.o: ../lib/converter_functions.c
	$(CC) $(CFLAGS) -c ../lib/converter_functions.c $(TEXT_INCLUDE_DIRS)

field_info.o: ../lib/field_info.c
	$(CC) $(CFLAGS) -c ../lib/field_info.c $(TEXT_INCLUDE_DIRS)

clean:
	-rm -f *.o

