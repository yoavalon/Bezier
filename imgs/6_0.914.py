d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.NE, Length.medium)

d.end()
