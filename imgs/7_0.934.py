d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(3,3)

d.end()
