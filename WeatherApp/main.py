
import modules.settings as set

# import modules.widget as widget


# print(set.table_not_empty())

if not set.table_not_empty():
    import modules.reg as reg
    reg.reg_window.mainloop()
else:
    import modules.widget as widget 
    widget.widget.mainloop()
    # import modules.big_screen as big_screen
    # big_screen.big_screen.mainloop()

#widget.widget.mainloop()
