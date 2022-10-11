d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(3,2)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)

d.end()
