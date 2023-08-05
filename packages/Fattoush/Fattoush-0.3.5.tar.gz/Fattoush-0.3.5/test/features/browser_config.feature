Feature: Browser Configuration
  As a test developer I want to be able to set a diverse
  variety of browser configurations to facilitate a wider
  testing environment


Scenario Outline: Flat desired capabilties

  Given I pass desired capabilites of "<caps>"
  When fattoush creates a configurations from this
  Then the configuration name is "<name>"

  Examples:
    | name                          | caps                                      |
    | browser=googlechrome          | {"browser": "googlechrome"}               |
    | browser=googlechrome;foo=bar  | {"browser": "googlechrome", "foo": "bar"} |


Scenario: Nested desired capabilties

  Given I pass desired capabilites of "{"browser": "googlechrome", "foo": {"bar" : ["baz"]}}"
  When fattoush creates a configurations from this
  Then it does not crash
