d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(2,3)
d.straight_line(Direction.NW, Length.long)
d.position_pen(2,2)
d.position_pen(1,2)

d.end()
