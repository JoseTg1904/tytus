from Hash import TablaHash

class Database:
    """
    @description Constructor, llamado por el método createDatabase(nombre: str) -> int
    @param nombre, debe cumplir con las reglas de identificadores de SQL
    @return
        0 operación exitosa
        1 error en la operación 
        2 base de datos existente
    """
    def __init__(self, name):
        self.name = name
        self.tables = []

    """
    alterDatabase(databaseNew) -> int
    @param databaseNew, nombre nuevo de la base de datos
    """
    def setName(self, databaseNew):
        self.name = databaseNew

    def getName(self):
        return self.name

    def getTable(self, indice):
        return self.tables[indice]

    """
    prototype method
    """
    def buscarTable(self, name):
        if len(self.tables) != 0:
            for table in self.tables:
                if name == table.getName():
                    #encontrada
                    return self.tables.index(table)
        return None

    def dropTable(self, indice):
        try:
            self.tables.pop(indice)
            return 0
        except: 
            return 1

    """
    createTable(size(default), database, table, nCols) -> int
    """
    def createTable(self, size, table, nCols):
        try:
            if self.buscarTable(table) != None:
                print("Tabla existente")
                return 2
            else:
                hashTable = TablaHash(6, table, nCols)
                self.tables.append(hashTable)
                return 0
        except: 
            print("Error en la operación")
            return 1
    
    def showTables(self):
        tables = []
        for table in self.tables:
            tables.append(table.getName())
        return tables

    def alterAddPK(self, name, columns):
        try:
            if self.buscarTable(name) != None:
                index = self.buscarTable(name)
                table = self.tables[index]
                table.alterAddPK(columns)
            else:
                print("Tabla Inexistente")
                return 2
        except: 
            print("Error en la operación")
            return 1

    def insert(self, name, register):
        try:
            if self.buscarTable(name) != None:
                index = self.buscarTable(name)
                table = self.tables[index]
                table.insert(table, register)
            else:
                print("Tabla Inexistente")
                return 2
        except: 
            print("Error en la operación")
            return 1

    ##16/12/2020 CRISTIAN
    def extractTable2(self,table):
        try:
            if self.buscarTable(table) != None:
                print("Tabla existente")
                index = self.buscarTable(table)
                table = self.tables[index]
                table.printTbl()               
                return 2
            else:
                print("Tabla NO existente")
                return 0
        except: 
            print("Error en la operación")
            return 1        

    def extractRangeTable2(self,table,lower,upper):
        pass              

