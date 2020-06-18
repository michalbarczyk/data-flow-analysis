def thread_binary_expr(expr_node_pointer):
    thread_expr(expr_node_pointer.left_op)
    thread_expr(expr_node_pointer.right_op)
    last_node_pointer.successor = expr_node_pointer
    last_node_pointer = expr_node_pointer