import traceback
from unittest.mock import MagicMock, call
#from src.edu.upc.ac.marker.ClasesCorrector import SuperClassForTests
#from src.edu.upc.etsetb.arqsoft.spreadsheet.usecases.marker.spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker
from ClasesCorrector import SuperClassForTests
from spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker


class NumberContentTest(SuperClassForTests):

    numErrorsBefore = 0;

    numInstances = 0;

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        NumberContentTest.numInstances = NumberContentTest.numInstances + 1
        self.instance=SpreadSheetFactoryForChecker.create_spreadsheet_controller()
        if NumberContentTest.numInstances == 1:
            NumberContentTest.numErrorsBefore = len(SuperClassForTests.indErrors)

    def setUpClass():
        # SuperClassForTests.nota = {}
        NumberContentTest.nota = 0.0
        print("\nMarking editing a cell with a number content (NumberContentTest)")
        print("***********************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "NumberContent")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        NumberContentTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0;

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_set_cell_content_number_content(self):
        valor_total = 10
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with numerical content. Value: " + str(valor_total))
        try:
            float_val=2.5
            self.instance.set_cell_content("C1",float_val)
            content = self.instance.get_cell_content_as_float("C1")
            error = self.sAssertEquals(float_val,content,valor_total,"The cell " \
                                       + "should contain the value: " + str(float_val)+ ". Instead, it contains " \
                                       + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)
