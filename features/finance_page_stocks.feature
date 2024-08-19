Feature: Finance Page Stocks

  Background:
    Given Open the finance page
    Then Verify the finance page is loaded by following data
      | element | value                                                                  |
      | title   | Google Finance - Stock Market Prices, Real-time Quotes & Business News |
    And Retrieve the stock symbols listed under the section "You may be interested in info"
    And Compare the retrieved stock symbols with the following data
      | symbol |
      | NFLX   |
      | MSFT   |
      | TSLA   |

  @default
  Scenario: Compare and print all results
    Then Print all stock symbols that are present in the actual data but not in the given test data
    And Print all stock symbols that are present in the given test data but not in the actual data

  @not_in_test
  Scenario: Compare and print results that are in actual data but not in given test data
    Then Print all stock symbols that are present in the actual data but not in the given test data

  @not_in_actual
  Scenario: Compare and print results that are in given test data but not in actual data
    Then Print all stock symbols that are present in the given test data but not in the actual data