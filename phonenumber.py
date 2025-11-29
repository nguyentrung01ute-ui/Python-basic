import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os

DATA_FILE = "contacts.json"
GROUP_FILE = "groups.json"

# ===================== DỮ LIỆU =====================
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            return {name: tuple(info) for name, info in raw_data.items()}
    return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({name: list(info) for name, info in contacts.items()}, f, ensure_ascii=False, indent=2)

def load_groups():
    if os.path.exists(GROUP_FILE):
        with open(GROUP_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_groups(groups):
    with open(GROUP_FILE, "w", encoding="utf-8") as f:
        json.dump(groups, f, ensure_ascii=False, indent=2)

contacts = load_contacts()
groups = load_groups()
phone_set = set(info[0] for info in contacts.values())

# ===================== CHỨC NĂNG =====================
def add_contact():
    name = simpledialog.askstring("Thêm liên hệ", "Nhập tên:")
    if not name: return
    phone = simpledialog.askstring("Thêm liên hệ", "Nhập số điện thoại:")
    if not phone: return
    email = simpledialog.askstring("Thêm liên hệ", "Nhập email:")
    if not email: return
    address = simpledialog.askstring("Thêm liên hệ", "Nhập địa chỉ:")
    if not address: return

    if phone in phone_set:
        messagebox.showwarning("Lỗi", "Số điện thoại đã tồn tại!")
        return

    contacts[name] = (phone, email, address)
    phone_set.add(phone)
    # Tạo nhóm tự động theo địa chỉ nếu chưa có
    if address not in groups:
        groups[address] = []
    groups[address].append(name)

    save_contacts(contacts)
    save_groups(groups)
    refresh_tree()
    messagebox.showinfo("Thành công", f"Đã thêm {name}.")

def delete_contact():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Chọn liên hệ để xóa")
        return
    name = tree.item(selected[0])['values'][0]
    phone_set.discard(contacts[name][0])
    contacts.pop(name)
    for members in groups.values():
        if name in members:
            members.remove(name)
    save_contacts(contacts)
    save_groups(groups)
    refresh_tree()
    messagebox.showinfo("Thành công", f"Đã xóa {name}.")

def refresh_tree(sort_by=None, reverse=False):
    for row in tree.get_children():
        tree.delete(row)
    items = [(name, *info) for name, info in contacts.items()]
    if sort_by is not None:
        items.sort(key=lambda x: x[sort_by], reverse=reverse)
    for item in items:
        tree.insert("", tk.END, values=item)

def search_contact():
    keyword = simpledialog.askstring("Tìm kiếm", "Nhập từ khóa:")
    if not keyword: return
    keyword = keyword.lower()
    results = [(name, *info) for name, info in contacts.items()
               if keyword in name.lower() or keyword in info[0].lower()
               or keyword in info[1].lower() or keyword in info[2].lower()]
    for row in tree.get_children():
        tree.delete(row)
    for item in results:
        tree.insert("", tk.END, values=item)

# ===================== QUẢN LÝ NHÓM =====================
def create_group():
    group_name = simpledialog.askstring("Tạo nhóm", "Nhập tên nhóm:")
    if not group_name: return
    if group_name in groups:
        messagebox.showwarning("Lỗi", "Nhóm đã tồn tại.")
        return
    groups[group_name] = []
    save_groups(groups)
    messagebox.showinfo("Thành công", f"Đã tạo nhóm {group_name}")

def add_to_group():
    group_name = simpledialog.askstring("Thêm vào nhóm", "Nhập tên nhóm:")
    if not group_name or group_name not in groups:
        messagebox.showerror("Lỗi", "Nhóm không tồn tại")
        return
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Chọn liên hệ để thêm vào nhóm")
        return
    for s in selected:
        name = tree.item(s)['values'][0]
        if name not in groups[group_name]:
            groups[group_name].append(name)
    save_groups(groups)
    messagebox.showinfo("Thành công", f"Đã thêm liên hệ vào nhóm {group_name}")

def show_groups():
    lst = []
    for g, members in groups.items():
        lst.append(f"{g} ({len(members)} liên hệ): {', '.join(members)}")
    messagebox.showinfo("Nhóm", "\n".join(lst))

def show_statistics():
    city_count = {}
    for info in contacts.values():
        city_count[info[2]] = city_count.get(info[2], 0) + 1
    group_count = {g: len(members) for g, members in groups.items()}
    text = "Số liên hệ theo địa chỉ:\n"
    for city, count in city_count.items():
        text += f"- {city}: {count}\n"
    text += "\nSố lượng liên hệ theo nhóm:\n"
    for g, count in group_count.items():
        text += f"- {g}: {count}\n"
    messagebox.showinfo("Thống kê", text)

# ===================== SẮP XẾP TREEVIEW KHI CLICK HEADER =====================
sort_orders = [False]*4  # Theo thứ tự cột (Tên,SĐT,Email,Địa chỉ)

def treeview_sort_column(col_idx):
    global sort_orders
    sort_orders[col_idx] = not sort_orders[col_idx]
    refresh_tree(sort_by=col_idx, reverse=sort_orders[col_idx])

# ===================== GIAO DIỆN =====================
root = tk.Tk()
root.title("Mini Contact Manager Advanced GUI")
root.geometry("750x500")

frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

tk.Button(frame_buttons, text="Thêm liên hệ", command=add_contact).pack(side=tk.LEFT, padx=2)
tk.Button(frame_buttons, text="Xóa liên hệ", command=delete_contact).pack(side=tk.LEFT, padx=2)
tk.Button(frame_buttons, text="Tìm kiếm", command=search_contact).pack(side=tk.LEFT, padx=2)
tk.Button(frame_buttons, text="Tạo nhóm", command=create_group).pack(side=tk.LEFT, padx=2)
tk.Button(frame_buttons, text="Thêm vào nhóm", command=add_to_group).pack(side=tk.LEFT, padx=2)
tk.Button(frame_buttons, text="Xem nhóm", command=show_groups).pack(side=tk.LEFT, padx=2)
tk.Button(frame_buttons, text="Thống kê", command=show_statistics).pack(side=tk.LEFT, padx=2)

# Treeview danh bạ
columns = ("Tên","SĐT","Email","Địa chỉ")
tree = ttk.Treeview(root, columns=columns, show='headings')
for i, col in enumerate(columns):
    tree.heading(col, text=col, command=lambda _i=i: treeview_sort_column(_i))
    tree.column(col, width=150)
tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

refresh_tree()

root.mainloop()
