from behave import given, when, then


def eq(a, b, msg='{a} != {b}'):
    if a != b:
        raise AssertionError(msg.format(a=a, b=b))


@then(u'I should see login form')
def i_should_see(context):
    assert context.browser.is_element_present_by_css('form')


@when(r'I visit home page')
def i_visit_url(context):
    br = context.browser
    br.visit("http://localhost:8081/")


@given('a user')
def step_impl(context):
    from django.contrib.auth.models import User
    u = User(username='foo', email='foo@example.com')
    u.set_password('bar')
    u.save()


@when('I log in')
def step_impl(context):
    br = context.browser
    br.visit('http://localhost:8081/login/')
    br.find_by_css('#username').first.fill('foo')
    br.find_by_css('#password').first.fill('bar')
    br.find_by_value('Log in').first.click()


@then('I see index page')
def step_impl(context):
    br = context.browser
    eq(br.url, "http://localhost:8081/")
    assert br.url == "http://localhost:8081/"


@when('I gave not valid data')
def step_impl(context):
    br = context.browser
    br.visit('http://localhost:8081/login/')
    br.find_by_css('#username').first.fill('foo1')
    br.find_by_css('#password').first.fill('bar1')
    br.find_by_value('Log in').first.click()


@then('I see login form and see error message')
def step_impl(context):
    br = context.browser
    eq(br.url, 'http://localhost:8081/login/')
    if br.is_element_present_by_css('form') and br.is_element_present_by_css('.errorlist'):
        assert True
    else:
        assert False
