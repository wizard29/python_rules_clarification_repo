load("@pip_extensions//:requirements.bzl", "requirement")

py_binary(
    name = "python_application",
    srcs = ["python_application.py"],
    deps = [requirement("nicegui")],
)

py_test(
    name = "pylint_test",
    srcs = ["pylint_test.py"],
    data = [
        "python_application.py",
        "//entry_points:pylint",
    ],
    env = {
        "ENTRY_POINT": "$(rlocationpath //entry_points:pylint)",
        "PYLINTHOME": "./.pylint_home",
    },
    deps = ["@rules_python//python/runfiles"],
)
