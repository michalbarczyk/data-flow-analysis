def thread_if_statement(if_node_pointer):
    thread_expr(if_node_pointer.condition)
    last_node_pointer.succ = if_node_pointer
    end_if_join_node = generate_join_node()
    last_node_pointer = aux_last_node
    thread_block(if_node_pointer.then_part)
    if_node_pointer.true_succ = aux_last_node.succ
    last_node_pointer.succ = end_if_join_node
    last_node_pointer = aux_last_node
    thread_block(if_node_pointer.else_part)
    if_node_pointer.false_succ = aux_last_node.succ
    last_node_pointer.succ = end_if_join_node