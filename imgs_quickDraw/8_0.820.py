d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
