"""
This module contains tools for managing Trello boards, lists, cards, and workspaces.
"""

from server.tools import attachment, board, card, checklist, comment, label, list, member, webhook, workspace


def register_tools(mcp):
    """Register tools with the MCP server."""
    # Board Tools
    mcp.add_tool(board.get_board)
    mcp.add_tool(board.get_boards)
    mcp.add_tool(board.get_board_labels)
    mcp.add_tool(board.create_board_label)
    mcp.add_tool(board.create_board)
    mcp.add_tool(board.update_board)
    mcp.add_tool(board.delete_board)

    # List Tools
    mcp.add_tool(list.get_list)
    mcp.add_tool(list.get_lists)
    mcp.add_tool(list.create_list)
    mcp.add_tool(list.update_list)
    mcp.add_tool(list.delete_list)

    # Card Tools
    mcp.add_tool(card.get_card)
    mcp.add_tool(card.get_cards)
    mcp.add_tool(card.create_card)
    mcp.add_tool(card.update_card)
    mcp.add_tool(card.delete_card)

    # Checklist Tools
    mcp.add_tool(checklist.get_checklist)
    mcp.add_tool(checklist.get_card_checklists)
    mcp.add_tool(checklist.create_checklist)
    mcp.add_tool(checklist.update_checklist)
    mcp.add_tool(checklist.delete_checklist)
    mcp.add_tool(checklist.add_checkitem)
    mcp.add_tool(checklist.update_checkitem)
    mcp.add_tool(checklist.delete_checkitem)

    # Label Tools
    mcp.add_tool(label.update_label)
    mcp.add_tool(label.delete_label)
    mcp.add_tool(label.get_card_labels)
    mcp.add_tool(label.add_label_to_card)
    mcp.add_tool(label.remove_label_from_card)

    # Comment Tools
    mcp.add_tool(comment.get_card_comments)
    mcp.add_tool(comment.get_card_actions)
    mcp.add_tool(comment.add_comment)
    mcp.add_tool(comment.update_comment)
    mcp.add_tool(comment.delete_comment)
    mcp.add_tool(comment.get_board_actions)

    # Attachment Tools
    mcp.add_tool(attachment.get_card_attachments)
    mcp.add_tool(attachment.attach_url)
    mcp.add_tool(attachment.delete_attachment)
    mcp.add_tool(attachment.set_attachment_as_cover)

    # Member Tools
    mcp.add_tool(member.get_board_members)
    mcp.add_tool(member.add_board_member)
    mcp.add_tool(member.update_board_member)
    mcp.add_tool(member.remove_board_member)
    mcp.add_tool(member.get_workspace_members)
    mcp.add_tool(member.get_member)
    mcp.add_tool(member.get_card_members)
    mcp.add_tool(member.add_card_member)
    mcp.add_tool(member.remove_card_member)

    # Webhook Tools
    mcp.add_tool(webhook.create_webhook)
    mcp.add_tool(webhook.get_webhook)
    mcp.add_tool(webhook.list_webhooks)
    mcp.add_tool(webhook.update_webhook)
    mcp.add_tool(webhook.delete_webhook)

    # Workspace Tools
    mcp.add_tool(workspace.get_workspaces)
    mcp.add_tool(workspace.get_workspace)
    mcp.add_tool(workspace.get_workspace_boards)
    mcp.add_tool(workspace.create_workspace)
    mcp.add_tool(workspace.update_workspace)
    mcp.add_tool(workspace.delete_workspace)
