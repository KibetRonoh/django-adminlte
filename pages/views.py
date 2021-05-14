from django.shortcuts import render


def calendar(request):
    return render(request, 'adminlte/pages/calendar.html')


def gallery(request):
    return render(request, 'adminlte/pages/gallery.html')


def kanban(request):
    return render(request, 'adminlte/pages/kanban.html')


def widgets(request):
    return render(request, 'adminlte/pages/widgets.html')


def flot(request):
    return render(request, 'adminlte/pages/charts/flot.html')


def uplot(request):
    return render(request, 'adminlte/pages/charts/uplot.html')


def inline(request):
    return render(request, 'adminlte/pages/charts/inline.html')


def chartjs(request):
    return render(request, 'adminlte/pages/charts/chartjs.html')


def four04(request):
    return render(request, 'adminlte/pages/examples/404.html')


def five00(request):
    return render(request, 'adminlte/pages/examples/500.html')


def blank(request):
    return render(request, 'adminlte/pages/examples/blank.html')


def contact_us(request):
    return render(request, 'adminlte/pages/examples/contact-us.html')


def contacts(request):
    return render(request, 'adminlte/pages/examples/contacts.html')


def e_commerce(request):
    return render(request, 'adminlte/pages/examples/e-commerce.html')


def faq(request):
    return render(request, 'adminlte/pages/examples/faq.html')


def forgot_password(request):
    return render(request, 'adminlte/pages/examples/forgot-password.html')


def forgot_password_v2(request):
    return render(request, 'adminlte/pages/examples/forgot-password-v2.html')


def invoice(request):
    return render(request, 'adminlte/pages/examples/invoice.html')


def invoice_print(request):
    return render(request, 'adminlte/pages/examples/invoice-print.html')


def language_menu(request):
    return render(request, 'adminlte/pages/examples/language-menu.html')


def legacy_user_menu(request):
    return render(request, 'adminlte/pages/examples/legacy-user-menu.html')


def lockscreen(request):
    return render(request, 'adminlte/pages/examples/lockscreen.html')


def login(request):
    return render(request, 'adminlte/pages/examples/login.html')


def login_v2(request):
    return render(request, 'adminlte/pages/examples/login-v2.html')


def pace(request):
    return render(request, 'adminlte/pages/examples/pace.html')


def profile(request):
    return render(request, 'adminlte/pages/examples/profile.html')


def project_add(request):
    return render(request, 'adminlte/pages/examples/project-add.html')


def project_detail(request):
    return render(request, 'adminlte/pages/examples/project-detail.html')


def project_edit(request):
    return render(request, 'adminlte/pages/examples/project-edit.html')


def projects(request):
    return render(request, 'adminlte/pages/examples/projects.html')


def recover_password(request):
    return render(request, 'adminlte/pages/examples/recover-password.html')


def recover_password_v2(request):
    return render(request, 'adminlte/pages/examples/recover-password-v2.html')


def register(request):
    return render(request, 'adminlte/pages/examples/register.html')


def register_v2(request):
    return render(request, 'adminlte/pages/examples/register-v2.html')


def advanced(request):
    return render(request, 'adminlte/pages/forms/advanced.html')


def editors(request):
    return render(request, 'adminlte/pages/forms/editors.html')


def general(request):
    return render(request, 'adminlte/pages/forms/general.html')


def validation(request):
    return render(request, 'adminlte/pages/forms/validation.html')


def boxed(request):
    return render(request, 'adminlte/pages/layouts/boxed.html')


def collapsed_sidebar(request):
    return render(request, 'adminlte/pages/layouts/collapsed-sidebar.html')


def fixed_footer(request):
    return render(request, 'adminlte/pages/layouts/fixed-footer.html')


def compose(request):
    return render(request, 'adminlte/pages/mailbox/compose.html')


def mailbox(request):
    return render(request, 'adminlte/pages/mailbox/mailbox.html')


def read_mail(request):
    return render(request, 'adminlte/pages/mailbox/read-mail.html')


def fixed_sidebar(request):
    return render(request, 'adminlte/pages/layouts/fixed-sidebar.html')


def fixed_sidebar_custom(request):
    return render(request, 'adminlte/pages/layouts/fixed-sidebar-custom.html')


def fixed_topnav(request):
    return render(request, 'adminlte/pages/layouts/fixed-topnav.html')


def top_nav(request):
    return render(request, 'adminlte/pages/layouts/top-nav.html')


def top_nav_sidebar(request):
    return render(request, 'adminlte/pages/layouts/top-nav-sidebar.html')


def enhanced(request):
    return render(request, 'adminlte/pages/search/enhanced.html')


def enhanced_results(request):
    return render(request, 'adminlte/pages/search/enhanced-results.html')


def simple_search(request):
    return render(request, 'adminlte/pages/search/simple-search.html')


def simple_results(request):
    return render(request, 'adminlte/pages/search/simple-results.html')


def data(request):
    return render(request, 'adminlte/pages/tables/data.html')


def jsgrid(request):
    return render(request, 'adminlte/pages/tables/jsgrid.html')


def simple(request):
    return render(request, 'adminlte/pages/tables/simple.html')


def icons(request):
    return render(request, 'adminlte/pages/ui/icons.html')


def buttons(request):
    return render(request, 'adminlte/pages/ui/buttons.html')


def general(request):
    return render(request, 'adminlte/pages/ui/general.html')


def modals(request):
    return render(request, 'adminlte/pages/ui/modals.html')


def navbar(request):
    return render(request, 'adminlte/pages/ui/navbar.html')


def ribbons(request):
    return render(request, 'adminlte/pages/ui/ribbons.html')


def sliders(request):
    return render(request, 'adminlte/pages/ui/sliders.html')


def timeline(request):
    return render(request, 'adminlte/pages/ui/timeline.html')
