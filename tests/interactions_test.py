from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open_url()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of list has not been changer"
            assert grid_before != grid_after, "The order of grid has not been changer"

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open_url()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "No elements were selected"
            assert len(item_grid) > 0, "No elements were selected"

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open_url()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, "Maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "Minimum size not equal to '150px', '150px'"
            assert max_resize != min_resize, "Resizable has not been changed"

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open_url()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', "the elements has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open_url()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == "Drop here", "the dropped element has been accepted"
            assert accept == "Dropped!", "the dropped element has not been accepted"

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open_url()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == "Dropped!", "the elements texts has not been changed"
            assert not_greedy_inner == "Dropped!", "the elements texts has not been changed"
            assert greedy == "Outer droppable", "the elements texts has been changed"
            assert greedy_inner == "Dropped!", "the elements texts has not been changed"

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open_url()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable("will")
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable("not_will")
            assert will_after_move != will_after_revert, "the elements has not reverted"
            assert not_will_after_move == not_will_after_revert, "the elements has  reverted"

    class TestDraggablePage:

        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open_url()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "The position of the box has not been changed"

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open_url()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, "Box position has not changed or there has been a shift in the y-axis"
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, "Box position has not changed or there has been a shift in the y-axis"
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, "Box position has not changed or there has been a shift in the x-axis"
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, "Box position has not changed or there has been a shift in the x-axis"
