d = DslBezier()

d.position_pen(2,1)
d.position_pen(3,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SW, Length.short)

d.end()
