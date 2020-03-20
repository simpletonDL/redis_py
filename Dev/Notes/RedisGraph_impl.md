## Entity

```
typedef struct {
	union {
		SIValue s;
		Node n;
		Edge e;
	} value;
	RecordEntryType type;
} Entry;
```

```
typedef struct
{
    Entity *entity;    /* MUST be the first property of Edge. */
    const char *label; /* Label attached to node */
    int labelID;       /* Label ID. */
    GrB_Matrix mat;    /* Label matrix, associated with node. */
} Node;

typedef struct
{
    EntityID id;                // Unique id
    int prop_count;             // Number of properties.
    EntityProperty *properties; // Key value pair of attributes.
} Entity;
```

## Record
```
// Record = массив Entry
typedef Entry *Record;
```

```
// Представляет значение атрибута
typedef struct SIValue {
	union {
		int64_t longval;
		double doubleval;
		char *stringval;
		void *ptrval;
		struct SIValue *array;
	};
	SIType type;
	SIAllocation allocation;
} SIValue;
```