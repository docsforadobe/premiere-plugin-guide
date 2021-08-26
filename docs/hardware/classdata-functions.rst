.. _hardware/classdata-functions:

ClassData Functions
################################################################################

All plug-in types that support media can use these callbacks to share information associated with their classID.

For example, these plugins can confirm their hardware is present and operational using the ClassData functions.

They all call ``getClassData`` during initialization. If ``getClassData`` returns 0, the module checks for and initialize the hardware.

It then calls setClassData to store information about the current context. Use handles, not pointers, for storing info.

.. code-block:: c++

  typedef struct {
    SetClassDataFunc  setClassData;
    GetClassDataFunc  getClassData;
  } ClassDataFuncs, *ClassDataFuncsPtr;

+------------------+---------------------------------------------------------------------------------+
| **Function**     | **Description**                                                                 |
+------------------+---------------------------------------------------------------------------------+
| ``setClassData`` | Writes class data, destroys previous data.                                      |
|                  |                                                                                 |
|                  | ::                                                                              |
|                  |                                                                                 |
|                  |   int setClassData (                                                            |
|                  |     unsigned int  theClass,                                                     |
|                  |     void          *info);                                                       |
|                  |                                                                                 |
|                  | - ``theClass`` - the class being set. Use a unique 4-byte code.                 |
|                  | - ``info`` - the class data to be set. It can be used as a pointer or a handle. |
|                  |                                                                                 |
|                  | Note that all plugins that share the data must use the same data structure.     |
+------------------+---------------------------------------------------------------------------------+
| ``getClassData`` | Retrieves the class data for the given class.                                   |
|                  |                                                                                 |
|                  | ::                                                                              |
|                  |                                                                                 |
|                  |   int getClassData (                                                            |
|                  |     unsigned int  theClass);                                                    |
|                  |                                                                                 |
|                  | - ``theClass`` - the class for which to retrieve data.                          |
+------------------+---------------------------------------------------------------------------------+
