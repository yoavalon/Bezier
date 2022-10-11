d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
