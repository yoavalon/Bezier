d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,3)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)

d.end()
