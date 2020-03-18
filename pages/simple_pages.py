from pages.page_with_title import create_page_class

AgreementPage = create_page_class(
	'Согласие на обработку персональных данных',
	'content-header__title')

RatingPage = create_page_class(
	'Рейтинг блогов и сообществ', 
	'subsite_head__name')

AboutPage = create_page_class(
	'TJ — блогплатформа',
	'content-header__title')

ConfigurePage = create_page_class(
	'Настройка ленты',
	'subsites_tune__header')