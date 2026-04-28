types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def delete_double_tickets (tickets):
    new_tickets ={}
    new_ticket = []   
    for n_str in tickets:
        str_tikets  =[] 
        for ticket in tickets[n_str]:
            if ticket in new_ticket:
                continue
            else:
                new_ticket.append(ticket)
                str_tikets.append(ticket)
                new_tickets[n_str] = str_tikets
    return new_tickets


def dictionary_merge_function (types, tickets):
    
    new_tickets = delete_double_tickets (tickets)
    tickets_by_type ={}
    for i in types.keys():        
        tickets_by_type[types[i]] = new_tickets[i]
     
    return tickets_by_type   