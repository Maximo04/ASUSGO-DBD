def querys(d_query):
    if d_query['function'] == 'R_U':
        return [f"select * from PERSON where MAIL like '{d_query['email']}';",
            f"select * from STUDENT where MAIL like '{d_query['email']}';"]
    elif d_query['function'] == 'W_U':
        return [f"insert into PERSON(NAME, MAIL, C_ABSCENCE, TYPE) values ('{d_query['name']}','{d_query['email']}',0,'0');",
            f"insert into STUDENT(NAME, MAIL, YEAR, C_ABSCENCE) values ('{d_query['name']}','{d_query['email']}','0',0);"]
    elif d_query['function'] == 'U_U':
        return [f"update STUDENT SET C_ABSCENCE = {d_query['c_abscence']}, `YEAR`='{d_query['year']}' WHERE MAIL like '{d_query['email']}';",
        f"update PERSON set C_ABSCENCE = {d_query['c_abscence']}, WHERE MAIL like '{d_query['email']}';"]
    elif d_query['function'] == 'R_S':
        return f"select * from STORAGE WHERE TYPE_ST = '{d_query['type']}';"
    elif d_query['function']  == 'W_S':
        return f"insert into STORAGE(DATE_ST, TEXT_ST,TYPE_ST) values ('{d_query['date']}','{d_query['text']}','{d_query['type']}');"
    elif d_query['function']== 'D_S':
        return f"delete from STORAGE where ID_ST = '{d_query['id']}';"
    elif d_query['function']== 'R_PDF_S':
        return [f"select * from PDF_STORAGE where NAME_PDF = '{d_query['name']}';",
            f"select * from PDF_STORAGE where TYPE_PDF_ST = '{d_query['type']}';",
            f"select NAME_PDF from PDF_STORAGE where ID_PDF_ST = '{d_query['id']}';"]
    elif d_query['function']== 'W_PDF_S':
        return f"insert into PDF_STORAGE(NAME_PDF,TYPE_PDF_ST) values ('{d_query['name']}','{d_query['type']}');"
    elif d_query['function']== 'D_PDF_S':
        return f"delete from PDF_STORAGE where ID_PDF_ST = '{d_query['id']}';"
    elif d_query['function'] == 'R_ABS':
        return f"select * from abs_detail WHERE mail like '{d_query['email']}';"
    elif d_query['function']  == 'W_ABS':
        return f"insert into abs_detail(mail,abs,justified,date) values ('{d_query['email']}',{d_query['abs']},{d_query['justified']},'{d_query['date']}');"
