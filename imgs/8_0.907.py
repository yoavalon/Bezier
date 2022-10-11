d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
