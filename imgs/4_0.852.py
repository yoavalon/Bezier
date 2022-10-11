d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)

d.end()
