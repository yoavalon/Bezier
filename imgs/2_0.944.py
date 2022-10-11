d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(0,0)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
