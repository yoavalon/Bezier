d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,0)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
