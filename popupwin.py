from my_lib import *
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tkinter GUI 주소록")
# window.geometry("450x120")
centerWindow(width=450, height=120, root_window=window)
window.resizable(False, False)

label = Label(window, text="원하는 메뉴 버튼을 클릭하세요.", font=("Arial", 15))
label.pack(side="top")
frm_menu = Frame(window, borderwidth=10, width=640, bd=20)
frm_menu.pack(side="bottom", fill="both")

# (1) 찾기 (2) 추가/변경 (3) 삭제 (4) 모두 보기 (5) 종료 :
btn_find_person = Button(frm_menu, text='찾기', padx=15, pady=10, width=10,
                         command=lambda root_window=window: popup_find_person_window(root_window))
btn_find_person.pack(side='left')

btn_update_person = Button(frm_menu, text='추가/변경', padx=15, pady=10, width=10,
                           command=lambda root_window=window: popup_update_person_window(root_window))
btn_update_person.pack(side='left')

btn_delete_person = Button(frm_menu, text='삭제', padx=15, pady=10, width=10,
                           command=lambda root_window=window: popup_delete_person_window(root_window))
btn_delete_person.pack(side='left')

btn_show_all = Button(frm_menu, text='모두 보기', padx=15, pady=10, width=10,
                      command=lambda root_window=window: popup_show_all_window(root_window))
btn_show_all.pack(side='left')


def on_closing():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        con.close()
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
