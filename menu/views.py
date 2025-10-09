from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu
from django.contrib import messages


def menu(request):
    menu_items = Menu.objects.all()

    # Получаем содержимое корзины из сессии
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    total_quantity = 0

    for item_id, quantity in cart.items():
        try:
            dish = Menu.objects.get(id=item_id)
            item_total = dish.price * quantity
            cart_items.append({
                'dish': dish,
                'quantity': quantity,
                'item_total': item_total,
            })
            total_price += item_total
            total_quantity += quantity
        except Menu.DoesNotExist:
            pass  # Если блюдо удалено, пропускаем

    context = {
        'menu': menu_items,
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'menu/menu.html', context)


def add_to_cart(request, dish_id):
    if request.method == 'POST':
        dish = get_object_or_404(Menu, id=dish_id)
        cart = request.session.get('cart', {})

        # Увеличиваем количество или добавляем новое блюдо
        if str(dish_id) in cart:
            cart[str(dish_id)] += 1
        else:
            cart[str(dish_id)] = 1

        request.session['cart'] = cart
        messages.success(request, f'{dish.name} добавлено в корзину!')
        return redirect('menu')  # Перенаправляем обратно на страницу меню
    return redirect('menu')


def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    messages.success(request, 'Корзина очищена!')
    return redirect('menu')
