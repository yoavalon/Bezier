d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SE, Length.medium)

d.end()
