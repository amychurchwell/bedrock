# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.firefox.new.download import DownloadPage

# These tests are classed as destructive and only run on staging, as the ?geo= param
# is only meant for testing and not really for use in production.


def test_download_button_displayed(base_url, selenium):
    page = DownloadPage(selenium, base_url, locale='ru', params='?geo=us').open()
    assert page.download_button.is_displayed
    assert page.download_button.is_transitional_link


# Firefox and Internet Explorer don't cope well with file prompts whilst using Selenium.
@pytest.mark.skip_if_firefox(reason='http://saucelabs.com/jobs/5a8a62a7620f489d92d6193fa67cf66b')
@pytest.mark.skip_if_internet_explorer(reason='https://github.com/SeleniumHQ/selenium/issues/448')
def test_click_download_button(base_url, selenium, locale='ru', params='?geo=us'):
    page = DownloadPage(selenium, base_url).open()
    thank_you_page = page.download_firefox()
    assert thank_you_page.seed_url in selenium.current_url


def test_yandex_download_button_displayed(base_url, selenium):
    page = DownloadPage(selenium, base_url, locale='ru', params='?geo=ru').open()
    assert page.download_button.is_displayed
    assert page.download_button.is_yandex_link


def test_other_platforms_modal(base_url, selenium):
    page = DownloadPage(selenium, base_url, params='?geo=us').open()
    modal = page.open_other_platforms_modal()
    assert modal.is_displayed
    modal.close()
