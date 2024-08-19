from behave import step

from pages.finance_page import FinancePage


@step("Open the finance page")
def open_finance_page(context):
    """
    Opens the finance page using the provided URL.
    :param context: The Behave context, which holds the web driver and other test data.
    """
    context.finance_page = FinancePage(context.driver)
    context.finance_page.open('https://www.google.com/finance/')


@step("Verify the finance page is loaded by following data")
def verify_finance_page_loaded(context):
    """
    Verifies that the finance page has loaded correctly by checking specific elements.
    :param context: The Behave context, which holds the web driver and other test data.
    """
    for row in context.table.rows:
        if row["element"] == "title":
            expected = row["value"]
            actual = context.finance_page.title
            assert expected == actual, f"Expected: {expected}, Actual: {actual}"


@step('Retrieve the stock symbols listed under the section "You may be interested in info"')
def retrieve_stock_symbols(context):
    """
    Retrieves stock symbols listed under a specific section of the finance page.
    :param context: The Behave context, which holds the web driver and other test data.
    """
    context.stock_symbols = context.finance_page.stock_symbols
    assert context.stock_symbols, "No stocks symbols were found"


@step("Compare the retrieved stock symbols with the following data")
def compare_stock_symbols(context):
    """
    Compares the retrieved stock symbols with those provided in the test data.
    :param context: The Behave context, which holds the web driver and other test data.
    """
    test_data = []
    for row in context.table.rows:
        test_data.append(row["symbol"])
    context.actual_not_in_test = [stock for stock in context.stock_symbols if stock not in test_data]
    context.test_not_in_actual = [stock for stock in test_data if stock not in context.stock_symbols]


@step("Print all stock symbols that are present in the actual data but not in the given test data")
def print_symbols_in_actual_not_in_test(context):
    """
    Prints stock symbols that are present in the actual data but not in the given test data.
    :param context: The Behave context, which holds the web driver and other test data.
    """
    context.logger.info(
        f"Stock symbols that are in actual stocks but not in given test data: {context.actual_not_in_test}")


@step("Print all stock symbols that are present in the given test data but not in the actual data")
def print_symbols_in_test_not_in_actual(context):
    """
    Prints stock symbols that are present in the given test data but not in the actual data.
    :param context: The Behave context, which holds the web driver and other test data.
    """
    context.logger.info(
        f"Stock symbols that are in given test data but not in actual stocks: {context.test_not_in_actual}")
