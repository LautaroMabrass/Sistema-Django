def importeTotal(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})
        for key, value in carro.items():
            total += float(value["precio"]) * int(value["cantidad"])
    return {"total":total}