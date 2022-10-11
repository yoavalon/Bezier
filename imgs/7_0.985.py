d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)

d.end()
