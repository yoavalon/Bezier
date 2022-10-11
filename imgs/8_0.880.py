d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.position_pen(1,2)

d.end()
