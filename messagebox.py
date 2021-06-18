import PIL
import tkinter as tk


class InfoMessageBox(tk.Toplevel):

    DEFAULT_ICON = b'R0lGODlhMgAyAOfkAAClxwGlxwKlxwOlxwSlxwWlxwalxwelxwilxgilxwmlxwqlxwulxw+kxQ2l\nxxClxhOlxxalxhalxxelxhelxxSmxxilxhWmxxmlxhmlxxqlxxulxximxxylxxmmxx+lxhymxyCm\nxyWmxyemxy+mxjCnxzGnxzamxTimxjmnxjunxj2oxz6ox0KnxkCox0CpyESoxkGpx0GpyEaoxkip\nxkmpx0qpx0yqx1SpxlasyFesyV6tyFyuyl2uymCuyV6vymSuyGGvyWGvymCwy2Kwy2ivyWWwymWw\ny2OxzGmwymaxy3CzzHW0zHa0zHS1zXK2z3m2zXu3znu3z363zX+3zYC3zYG4zoK4zoO5z4S5z4O6\n0IS60IW6z4W60Ia70Ie70Iq70Ie80Yi80Yi80ou80Yi90om90pHA1JXB1JbB1JjD1ZvD1ZvE1Z7F\n1qDF1aPH16rH1KXJ2avI1abK2a3J16/K2K7N26/O3LPN2rPO2rDP3bTP27XP3LTQ3bbQ3bfR3bjR\n3bjR3rnS3rrS3rvT37zU4L7U373V4L3V4b7V37/V4L7W4cDW4cTZ48ja5Mra48jb5Mnb5crb5Mrc\n5cvc5Mvc5czc5Mzc5c3c5Mrd5szd5cje6M3d5c7d5Mre6M/d5M/d5cve6M7e5s/e5dDe5tLe5NPf\n5dHg6NPg59Xj6dfk6trl69vl69vm69vm7Nzn7N7n7N3o7d7o7d/o7d7p7t/p7uDq7+Lq7uXs8Obs\n7+fs7+ns7ubt8eft8Ort7+fu8uju8enu8env8env8urv8u3v8erw8+vw8uvw8+zw8+3w8+3x8+7y\n9O/y9O/z9fH09vP19vX3+Pb3+Pf5+fj6+vn6+/n7+/r7+/r7/Pv7/Pv8/Pz8/fz9/f39/f39/v3+\n/v7+/v7+//7//////8UoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUo\nKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKMUoKCH5BAEKAP8ALAAAAAAyADIA\nAAj+AP8JHEiwYMFxCBMqNMiwoUODCrMti1UqVKhSspZlW/iwY0OE4IIdKlMDA4CTKDHUKIMoGDiE\nHmP+Q3jNUhQNKHPqPLlBCidsMGV+7IaJSICdSHUKQNKp2zihB8cd43IgqVWdCbwgCyp0nDhQLa6K\n1QmDlLinMsd988Nh7EkVc0Q5oiIgqQdAL2OqpbPALYAixBJqA2OVQZ28D7366eu2xC+F41RdZRDo\nbOJRbf2qgTzOllgPpNAyHIdMht+ThDgvGgsjmWiC47p1OX0yDuRnOdx+cQoRU1XaL3glJObEbwJQ\nr2deI0IbJYs3f9CYoG3k2utxl442355zQCfR48D+ReFOHuUUxOOC4fQ75pX79+5d+aANIrDAcYho\nM+KMcFqK5oqgNU4ZpxEwC3/j3IJAc2Q8NU42NZxmgjQINrLdDdogtIxJfgGxiy/FcNbGdhswg1As\ntA3QQANiQAZOEtzVglAp3PUBGTQjcGcKQqFwlwpkrWjXHCcIebJdCM5ARgh5RI5DY3M7OKXQGeTt\nOA6KzaUBGTc6kEcLQspY0FwikC3TAXcaLIMQNjSkCAtkqJBnQ4YzhUEbCdFApgd5ZghYCG1LvKTQ\nFuQZIiAwGZz2BmTXzMDdBsMICA4UpzkCWS8PcBcFYjNlIuRVDuAC2STcBXDJddUM4RYK1EBmB3fZ\nRFh3ECUGjBWElAmd8oQba5x2ACbJzcTNFWMd8Q1nL7FxWha8QSQMC2KdkCdn3yjh1wv2faTJBVcF\nAAh/zYjgFgXfJQZOHgta9cEdzHDTjTbEIMKDWwrwEU6wB3UDR7pWhYCDEDNQ4JcCcniDL0Td4FFB\neUhJsIfBXYFTyQoM58QCJpymlV4VBTBsgBXBcAXVTNs80sOnfgXwgyTcHNzVONVAwkQEfk3QRCTV\niDxyVN/kIggWLkCwEwQxaDGILse6vPNAClVDzCqfbLKJKKwYYw1HS7+MYNYBAQA7\n'

    def __init__(
            self, root, *args, btn_text="Ok",
            title="Info", msg="", icon=None, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.title(title)
        self.config(bg="#f8f5f1")
        self.resizable(False, False)
        self.msg = msg
        self.icon = icon
        self.btn_text = str(btn_text)


        # Main frame
        main_frm = tk.Frame(self,bg="#f8f5f1")
        main_frm.pack(expand=True, fill=tk.BOTH, padx=(10, 10), pady=10)

        # Icon
        if self.icon is not None:
            if isinstance(self.icon, tk.PhotoImage):
                h, w = self.icon.height(), self.icon.width()
                scale_w = w // 50
                scale_h = h // 50
                self.icon = self.icon.subsample(scale_w, scale_h)

            elif isinstance(self.icon, PIL.ImageFile.ImageFile):
                im = self.icon.resize((50, 50), PIL.Image.ANTIALIAS)
                self.icon = PIL.ImageTk.PhotoImage(im)

            else:
                raise ValueError(
                    f"can't use {self.icon} as icon: not a photo image"
                    )
        else:
            self.icon = tk.PhotoImage(data=self.DEFAULT_ICON)

        icon_label = tk.Label(main_frm, image=self.icon,bg="#f8f5f1")
        icon_label.grid(row=0, column=0, sticky=tk.NE)

        # Message label
        message = tk.Label(
            main_frm,
            text=self.msg,
            anchor=tk.W,
            justify=tk.LEFT,
            wraplength=350,
            bg="#f8f5f1",
            font='Helvetica 10 bold')
        message.grid(row=0, column=1, sticky=tk.NW)
        main_frm.rowconfigure(0, weight=1)

        # Button
        ok_btn = tk.Button(
            main_frm,
            #width=8,
            bg="#f8f5f1",
            text=self.btn_text,
            command=self.on_close,
            borderwidth=0,
            border=0,
            )
        ok_btn.bind('<KeyPress-Return>', func=self.on_close)
        ok_btn.grid(row=1, column=0, columnspan=2)

        # Modal dialog
        self.transient(master=root)
        self.grab_set()
        ok_btn.focus_set()
        self.deiconify()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self, *args):
        self.grab_release()
        self.destroy()
        return "ok"

