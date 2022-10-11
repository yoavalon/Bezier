d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,3)

d.end()
