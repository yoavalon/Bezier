d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.short)

d.end()
