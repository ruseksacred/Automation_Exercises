import pytest
from tests.test_basic import BasicTest

@pytest.mark.usefixtures("view_objects_creation")
class TestProducts(BasicTest):

    @pytest.mark.id9
    def test_search_product(self, view_objects_creation):
        pass