from django.shortcuts import render, redirect
from board.models import Board


def home(request):
    context = {}
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
    else:
        memberno = None
        membername = None

    context["member_no"] = memberno
    context["member_name"] = membername

    return render(request, "home.html", context)

def board(request):
    context = {}
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
    else:
        return redirect('/')

    context["member_no"] = memberno
    context["member_name"] = membername

    rsBoard = Board.objects.filter(usage_flag="1")
    context["rsBoard"] = rsBoard

    return render(request, "board_list.html", context)

def board_write(request):
 return render(request,"board_write.html")


def board_insert(request):
 btitle = request.GET['b_title']
 bnote = request.GET['b_note']
 bwriter = request.GET['b_writer']

 if btitle != "":
  rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
  return redirect('/board')
 else:
  return redirect('/board_write')

def board_view(request):
    bno = request.GET['b_no']

    rsData = Board.objects.get(b_no=bno)
    rsData.b_count += 1
    rsData.save()

    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        'rsDetail': rsDetail
    })

def board_edit(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_edit.html", {
        'rsDetail': rsDetail
    })
def board_update(request):
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter

        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return Response({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return Response({"success": False, "msg": "게시글 없음"})


def board_delete(request):
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()

    return redirect('/board')
