

def unique_order_id_generator(instance):
    code = 'TEACHER' + instance.full_name[0:2]

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(teacher_code=code).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return code
